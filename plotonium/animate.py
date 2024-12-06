import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from IPython.display import Image, display


# deternines which parameters are given and calculates the needed values accordingly
def _frames_and_interval(frames, fps, time):
    default_fps = 20
    default_time = 5 

    if frames and fps:
        interval = 1/fps
        time = frames/fps
    elif fps and time: 
        frames = fps * time
        interval = 1/fps
    elif frames and time:
        interval = time / frames
        fps = 1/interval
    else:
        print(f"ANIMATE: Parameters 'frames', 'fps', 'time' not given.")
        print(f"         Default values fps={default_fps} and time={default_time} taken")

        frames = default_fps * default_time
        fps = default_fps
        time = frames/fps
        interval = 1/default_fps

    interval *= 1000 # is given in ms
    return int(frames), interval, fps, time

# Modify the decorator to accept arguments
def animate(name="animation.gif", dpi=300, fps=None, frames=None, time=None, xlim=False, ylim=False, t_unit="one"):
    """
    Decorator for quick animations

    # Parameters
    name                Default is "animation.gif"
    dpi                 Resolution in pixel per inch. default: 300
    fps, frames, time   Only two should be specified, as the third will be redundant
    xlim, ylim          Axis limits
    t_unit              Unit in which the running parameter t is passed to the function.
                        Options are:
                            "one" (default) from zero to one
                            "frames" count of frame

    # Examples
    Simple animation
        @animate(name="test", dpi=50, xlim=(-5,5))  # Pass dpi as an argument to the decorator
        def myfunc(frame, fig, ax):
            x = np.linspace(0, 2 * np.pi, 300)
            y = np.sin(x + frame)
            ax.scatter(x, y)
    """
    def decorator(func):
        # create and customize plot
        fig, ax = plt.subplots(dpi=dpi)
        if xlim:
            ax.set_xlim(xlim)
        if ylim:
            ax.set_ylim(ylim)

        # calculate fps, total time, frame count and interval from given parameters
        frames_calc, interval_calc, fps_calc, time_calc = _frames_and_interval(frames, fps, time)
        print(f"ANIMATE: FPS:{fps_calc}, Total time:{time_calc:.1f}s, Frames:{frames_calc}, dpi:{dpi}")

        # animation using the decorate function "func"
        # also add a cute little progress indicator
        def animator(frame): 
            print(f"ANIMATE: progress {frame/frames_calc*100:.0f}%", end="\r")
            for line in ax.get_lines():
                line.remove()
            if t_unit == "one":
                t = frame / frames_calc
            elif t_unit == "seconds":
                t = frame / fps_calc
            else:
                t = frame
            func(t, fig, ax)

        anim = animation.FuncAnimation(fig=fig, func=animator, frames=frames_calc, interval=interval_calc)

        # add file extension to name if not already
        if name.endswith(".gif"):
            save_name = name
        else:
            save_name = name + ".gif"

        # save animation as gif
        anim.save(filename=save_name, writer="pillow", dpi=dpi)
        print(f"ANIMATE: Animation saved as '{save_name}'")
        plt.close(fig)
        display(Image(filename=save_name))

    return decorator

if __name__ == "__main__":
    @animate("test", dpi=100, fps=20, time=5)  # Pass dpi as an argument to the decorator
    def myfunc(t, fig, ax):
        x = np.linspace(0, 2 * np.pi, 300)
        y = np.sin(x + t)
        ax.plot(x, y, color="C0")
