import mpv
import asyncio
import cv2

async def check_idle_active(player):
    while True:
        idle_active = await player.get_property_async('idle-active')
        if not idle_active:
            break
        await asyncio.sleep(0.1)

async def get_current_time(player):
    while True:
        current_time = await player.get_property_async('time-pos')
        yield current_time
        await asyncio.sleep(0.1)

def play_video(video_path, timestamps):
    # Create an mpv player instance
    player = mpv.MPV()

    # Load the video file
    player.play(video_path)

    # Wait for the video to finish or press 'q' to exit
    loop = asyncio.get_event_loop()
    tasks = [check_idle_active(player), get_current_time(player)]

    async def process_frames():
        async for current_time in get_current_time(player):
            # Check if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Check if it's time to jump to the next timestamp
            for start, end in timestamps:
                if current_time >= start and current_time < end:
                    jump_to_time = end + 1  # Jump to 1 second after the specified end time
                    player.command("seek", jump_to_time, "absolute")

            # Check if all tasks are done (video is finished)
            if all(task.done() for task in tasks):
                break

    loop.run_until_complete(process_frames())

    # Terminate the mpv player
    player.terminate()


if __name__ == "__main__":
    video_path = '/home/rohit/Downloads/Telegram Desktop/Week 1/1.4 Git and Assignments.mp4'
    timestamps = [(732.0, 738.0), (1462.0, 1473.0), (1867.0, 1874.0),
                                 (2520.0, 2527.0), (2604.0, 2611.0), (4077.44, 4083.52),
                                 (4660.8, 4664.8), (5435.04, 5439.12)]
    play_video(video_path, timestamps)
