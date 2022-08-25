from moviepy.editor import VideoFIleClip

print("enter file name")
vc = input(":>> ")
videoc = VideoFIleClip(vc)

videoc.write_gif(vc)
