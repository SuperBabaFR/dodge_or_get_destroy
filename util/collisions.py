# Méthodes de collisions via les mathématiques (je suis pas si fort en math alors j'ai pas écrit ces méthodes)

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

def collide_circle_circle(c1_hitbox, c2_hitbox):
    x1, y1 = c1_hitbox["center"]
    r1 = c1_hitbox["radius"]

    x2, y2 = c2_hitbox["center"]
    r2 = c2_hitbox["radius"]

    dx = x1 - x2
    dy = y1 - y2
    distance_squared = dx * dx + dy * dy
    radius_sum = r1 + r2

    return distance_squared <= radius_sum * radius_sum
