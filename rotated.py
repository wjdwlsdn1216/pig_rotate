import math
import numpy as np


def rotate(origin, point, radian):
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(radian) * (px - ox) - math.sin(radian) * (py - oy)
    qy = oy + math.sin(radian) * (px - ox) + math.cos(radian) * (py - oy)
    return round(qx), round(qy)


def rotate_box_dot(x_cen, y_cen, width, height, theta):

    x_min = x_cen - width / 2
    y_min = y_cen - height / 2
    rotated_x1, rotated_y1 = rotate((x_cen, y_cen), (x_min, y_min), theta)
    rotated_x2, rotated_y2 = rotate((x_cen, y_cen), (x_min, y_min + height), theta)
    rotated_x3, rotated_y3 = rotate(
        (x_cen, y_cen), (x_min + width, y_min + height), theta
    )
    rotated_x4, rotated_y4 = rotate((x_cen, y_cen), (x_min + width, y_min), theta)

    answer_dict_ = {
        "Rx": np.array([rotated_x1, rotated_x2, rotated_x3, rotated_x4]),
        "Ry": np.array([rotated_y1, rotated_y2, rotated_y3, rotated_y4]),
    }

    return answer_dict_


def roi_in_box(img_width, img_height, rbox_dict, width_pad, height_pad):
    min_x = rbox_dict["xmin"]
    min_y = rbox_dict["ymin"]
    max_x = rbox_dict["xmax"]
    max_y = rbox_dict["ymax"]

    width_boundary = (img_width * width_pad, img_width * (1 - width_pad))
    height_boundary = (img_height * height_pad, img_height * (1 - height_pad))

    if (
        min_x >= width_boundary[0]
        and max_x <= width_boundary[1]
        and min_y >= height_boundary[0]
        and max_y <= height_boundary[1]
    ):
        return True
    else:
        return False


def cutter_fix_45(xc, yc, width, height):
    f_dist = (width + height) / np.sqrt(2)
    answer_dict_ = {
        "xmin": int(xc - f_dist / 2),
        "ymin": int(yc - f_dist / 2),
        "xmax": int(xc + f_dist / 2),
        "ymax": int(yc + f_dist / 2),
    }
    return answer_dict_