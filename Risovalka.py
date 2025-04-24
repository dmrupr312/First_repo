import pygame
import sys

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рисование пером с цветами")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

# Список доступных цветов
colors = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE, CYAN]
current_color_index = 0
current_color = colors[current_color_index]

# Параметры пера
pen_pos = [WIDTH // 2, HEIGHT // 2]  # Начальная позиция пера
pen_down = True  # Состояние пера (опущено/поднято)
pen_size = 3  # Размер пера
move_speed = 5  # Скорость движения пера

# Создаем поверхность для рисования
drawing_surface = pygame.Surface((WIDTH, HEIGHT))
drawing_surface.fill(WHITE)

# Шрифт для отображения информации
font = pygame.font.SysFont('Arial', 20)

def draw_info():
    # Отображаем текущую позицию, состояние пера и цвет
    color_name = {
        BLACK: "черный",
        RED: "красный",
        GREEN: "зеленый",
        BLUE: "синий",
        YELLOW: "желтый",
        PURPLE: "фиолетовый",
        CYAN: "голубой"
    }.get(current_color, "неизвестный")
    
    info_text = f"Позиция: ({pen_pos[0]}, {pen_pos[1]}) | Перо: {'опущено' if pen_down else 'поднято'} | Цвет: {color_name}"
    text_surface = font.render(info_text, True, BLACK)
    screen.blit(text_surface, (10, 10))
    
    # Рисуем маркер текущего положения пера текущим цветом
    pygame.draw.circle(screen, current_color, pen_pos, 5)
    
    # Отображаем текущий цвет в виде квадратика
    pygame.draw.rect(screen, current_color, (WIDTH - 40, 10, 30, 30))

def change_color():
    global current_color_index, current_color
    current_color_index = (current_color_index + 1) % len(colors)
    current_color = colors[current_color_index]

def main():
    global pen_pos, pen_down, current_color
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pen_down = not pen_down  # Переключаем состояние пера
                elif event.key == pygame.K_c:
                    drawing_surface.fill(WHITE)  # Очищаем экран
                elif event.key == pygame.K_BACKQUOTE:  # Клавиша Ё/~ (рядом с 1)
                    change_color()  # Меняем цвет
        
        # Обработка движения пера с помощью клавиш стрелок
        keys = pygame.key.get_pressed()
        old_pos = pen_pos.copy()
        
        if keys[pygame.K_LEFT]:
            pen_pos[0] = max(0, pen_pos[0] - move_speed)
        if keys[pygame.K_RIGHT]:
            pen_pos[0] = min(WIDTH, pen_pos[0] + move_speed)
        if keys[pygame.K_UP]:
            pen_pos[1] = max(0, pen_pos[1] - move_speed)
        if keys[pygame.K_DOWN]:
            pen_pos[1] = min(HEIGHT, pen_pos[1] + move_speed)
        
        # Если перо опущено и позиция изменилась - рисуем линию
        if pen_down and old_pos != pen_pos:
            pygame.draw.line(drawing_surface, current_color, old_pos, pen_pos, pen_size)
        
        # Отображаем все на экране
        screen.blit(drawing_surface, (0, 0))
        draw_info()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()