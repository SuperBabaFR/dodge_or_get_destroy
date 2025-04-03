

def collide_circle_rect(circle_rect, radius, rect):
    circle_x = circle_rect.centerx
    circle_y = circle_rect.centery

    closest_x = max(rect.left, min(circle_x, rect.right))
    closest_y = max(rect.top, min(circle_y, rect.bottom))

    dx = circle_x - closest_x
    dy = circle_y - closest_y

    return dx * dx + dy * dy < radius * radius
