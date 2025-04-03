

def collide_circle_rect(circle_hitbox, rect_hitbox):
    circle_x, circle_y = circle_hitbox["center"]
    radius = circle_hitbox["radius"]

    # Trouver le point du rectangle le plus proche du centre du cercle
    closest_x = max(rect_hitbox.left, min(circle_x, rect_hitbox.right))
    closest_y = max(rect_hitbox.top, min(circle_y, rect_hitbox.bottom))

    # Calculer la distance entre ce point et le centre du cercle
    dx = circle_x - closest_x
    dy = circle_y - closest_y
    distance_squared = dx * dx + dy * dy

    return distance_squared <= radius * radius
