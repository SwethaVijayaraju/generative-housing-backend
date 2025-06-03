import math
from typing import List, Tuple
from models.schemas import HousingRequest, Room


def assign_room_dimensions(room: Room) -> Room:
    """Assign square dimensions based on minimum area."""
    side = math.sqrt(room.min_area)
    room.width = side
    room.depth = side
    return room


def calculate_buildable_area(request: HousingRequest) -> Tuple[float, float]:
    """Calculate available width and depth after setbacks."""
    width = request.plot.width - 2 * request.setbacks.sides
    depth = request.plot.depth - request.setbacks.front - request.setbacks.back
    return width, depth


def place_room_in_layout(room: Room, x_cursor: float, y_cursor: float, setbacks) -> Room:
    """Position the room based on cursor location and setbacks."""
    room.x = x_cursor + setbacks.sides
    room.y = y_cursor + setbacks.back
    return room


def generate_layout(request: HousingRequest) -> List[Room]:
    buildable_width, buildable_depth = calculate_buildable_area(request)

    x_cursor, y_cursor = 0, 0
    max_row_height = 0
    placed_rooms = []

    for room in request.rooms:
        room = assign_room_dimensions(room)

        # If the room doesn't fit horizontally, move to the next row
        if x_cursor + room.width > buildable_width:
            x_cursor = 0
            y_cursor += max_row_height
            max_row_height = 0

        # If the room doesn't fit vertically, stop placing rooms
        if y_cursor + room.depth > buildable_depth:
            break

        room = place_room_in_layout(room, x_cursor, y_cursor, request.setbacks)
        placed_rooms.append(room)

        x_cursor += room.width
        max_row_height = max(max_row_height, room.depth)

    return placed_rooms
