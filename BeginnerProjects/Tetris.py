import pygame
import random

# Initialisierung
pygame.init()

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# Spielparameter
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT
GAME_AREA_LEFT = BLOCK_SIZE

# Tetromino-Formen
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# Tetromino-Klasse
class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = COLORS[SHAPES.index(shape)]
        self.rotation = 0

# Spielklasse
class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.fall_speed = 0.5  # Sekunden
        self.fall_time = 0

    def new_piece(self):
        shape = random.choice(SHAPES)
        return Tetromino(GRID_WIDTH // 2 - len(shape[0]) // 2, 0, shape)

    def valid_move(self, piece, x_offset=0, y_offset=0, rotation=0):
        shape = piece.shape
        if rotation != 0:
            shape = [list(row) for row in zip(*shape[::-1])] * rotation
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece.x + x + x_offset
                    new_y = piece.y + y + y_offset
                    if (new_x < 0 or new_x >= GRID_WIDTH or
                        new_y >= GRID_HEIGHT or
                        (new_y >= 0 and self.grid[new_y][new_x])):
                        return False
        return True

    def lock_piece(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[piece.y + y][piece.x + x] = piece.color
        self.clear_lines()
        self.current_piece = self.new_piece()
        if not self.valid_move(self.current_piece):
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_cleared += 1
                for y2 in range(y, 0, -1):
                    self.grid[y2] = self.grid[y2-1][:]
                self.grid[0] = [0 for _ in range(GRID_WIDTH)]
        if lines_cleared > 0:
            self.score += lines_cleared * 100 * self.level
            self.level = self.score // 1000 + 1
            self.fall_speed = max(0.05, 0.5 - (self.level - 1) * 0.05)

    def draw(self, screen):
        # Spielfeld
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(screen, GRAY,
                    (GAME_AREA_LEFT + x * BLOCK_SIZE, y * BLOCK_SIZE,
                     BLOCK_SIZE, BLOCK_SIZE), 1)
                if self.grid[y][x]:
                    pygame.draw.rect(screen, self.grid[y][x],
                        (GAME_AREA_LEFT + x * BLOCK_SIZE + 1, y * BLOCK_SIZE + 1,
                         BLOCK_SIZE - 2, BLOCK_SIZE - 2))

        # Aktuelles Stück
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.current_piece.color,
                        (GAME_AREA_LEFT + (self.current_piece.x + x) * BLOCK_SIZE + 1,
                         (self.current_piece.y + y) * BLOCK_SIZE + 1,
                         BLOCK_SIZE - 2, BLOCK_SIZE - 2))

        # Score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        level_text = font.render(f"Level: {self.level}", True, WHITE)
        screen.blit(score_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 10, 30))
        screen.blit(level_text, (GAME_AREA_LEFT + GRID_WIDTH * BLOCK_SIZE + 10, 70))

        if self.game_over:
            font = pygame.font.SysFont(None, 48)
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 24))

# Hauptfunktion
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    game = Tetris()

    running = True
    while running:
        screen.fill(BLACK)
        game.draw(screen)

        # Event-Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and game.valid_move(game.current_piece, -1):
                    game.current_piece.x -= 1
                if event.key == pygame.K_RIGHT and game.valid_move(game.current_piece, 1):
                    game.current_piece.x += 1
                if event.key == pygame.K_DOWN and game.valid_move(game.current_piece, 0, 1):
                    game.current_piece.y += 1
                if event.key == pygame.K_UP:
                    new_rotation = (game.current_piece.rotation + 1) % 4
                    if game.valid_move(game.current_piece, 0, 0, new_rotation):
                        game.current_piece.rotation = new_rotation
                        game.current_piece.shape = [list(row) for row in zip(*game.current_piece.shape[::-1])]
                if event.key == pygame.K_SPACE:
                    while game.valid_move(game.current_piece, 0, 1):
                        game.current_piece.y += 1
                    game.lock_piece(game.current_piece)

        # Fallen lassen
        current_time = pygame.time.get_ticks() / 1000
        if current_time - game.fall_time > game.fall_speed:
            if game.valid_move(game.current_piece, 0, 1):
                game.current_piece.y += 1
                game.fall_time = current_time
            else:
                game.lock_piece(game.current_piece)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
