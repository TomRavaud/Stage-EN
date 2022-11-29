import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True  # Render Matplotlib text with Tex

import cv2

T = np.load("./camera/src/state_estimation/pose_error.npy")
# print(T)


plt.figure(figsize=(6, 4))
print(np.mean(T[:, 1]))
print(np.count_nonzero(T[:, 1]>0.03))

plt.plot(T[:, 0]-T[0, 0], T[:, 1], "r+")

# plt.title(r"Pose estimation error on position")
plt.xlabel(r"Time (s)")
plt.ylabel(r"Error (m)")


plt.figure(figsize=(6, 4))
print(np.mean(T[:, 2]))
print(np.count_nonzero(T[:, 2]>0.03))

plt.plot(T[:, 0]-T[0, 0], T[:, 2], "b+")

# plt.title(r"Pose estimation error on position")
plt.xlabel(r"Time (s)")
plt.ylabel(r"Error (rad)")


# plt.figure(figsize=(6, 4))

# plt.plot(T[:, 0]-T[0, 0], T[:, 3], "g+")

# # plt.title(r"Pose estimation error on position")
# plt.xlabel(r"Time (s)")
# plt.ylabel(r"Translation (m)")


# plt.figure(figsize=(6, 4))

# plt.plot(T[:, 0]-T[0, 0], T[:, 4], "m+")

# # plt.title(r"Pose estimation error on position")
# plt.xlabel(r"Time (s)")
# plt.ylabel(r"Rotation (rad)")

# plt.figure(figsize=(6, 4))

# plt.plot(T[:, 3], T[:, 1], "m+")

# # plt.title(r"Pose estimation error on position")
# plt.xlabel(r"Time (s)")
# plt.ylabel(r"Rotation (rad)")

plt.show()