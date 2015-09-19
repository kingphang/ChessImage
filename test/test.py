# encoding: utf-8

from chessimage import ChessImage

# pixels = ChessImage.get_pixels("heart.png", 2)
# for row in pixels:
#     l = []
#     for r, g, b, a in row:
#         l.append("A" if a > 0 else " ")
#     print("".join(l))

# lattice = ChessImage.get_lattice_by_alpha("image.png",  8)
# for row in lattice:
#     print("".join(map(str, row)))

# ChessImage.get_lattice_image_by_alpha("map_world.png", "wrold_map.png", (226, 226, 226), 8)

# lattice = ChessImage.get_lattice_by_filter_color("map_world_blank_white.jpg", (255, 255, 255), 8)
# print(lattice)
# for row in lattice:
#     print("".join(map(str, row)))

# ChessImage.get_lattice_image_by_filter_color("map_world_blank_white.jpg", "map_world_blank_white_result.png", (255, 255, 255), (226, 226, 0), 8)

ChessImage.get_circle_points_drawing_doc_by_filter_color("map_world_blank_white.jpg", (255, 255, 255), "map_world_blank_white_doc.html", 3, "rgb(226, 226, 226)", 8)