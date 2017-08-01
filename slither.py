import pygame
import random

#initializaation 
pygame.init()

#colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
dark_green = (0, 100, 0)

#game display
display_width = 800
display_height = 600
FPS = 12
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")
clock = pygame.time.Clock()

#message to be written to screen
font = pygame.font.SysFont(None, 25)
def message_to_screen(msg, x, y, size, clr):
	font = pygame.font.SysFont(None, size)
	screen_text = font.render(msg, True, clr)
	game_display.blit(screen_text, (x, y)) 

#draw 
block_size = 25.0
def snake(snakelist, snakelen):
	if len(snakelist) > snakelen:
		del snakelist[0]

	for xny in snakelist:
		pygame.draw.rect(game_display, dark_green, [xny[0], xny[1], block_size, block_size])
		pygame.draw.rect(game_display, blue, [xny[0], xny[1], block_size / 4., block_size / 4.])

def apple(x, y):
	pygame.draw.rect(game_display, red, [x, y, block_size, block_size])

#main loop
game_exit = False
game_over = True

lead_x = display_width/2
lead_y = display_height/2
lead_x_change = 0
lead_y_change = 0
apple_x = round((random.randrange(0, display_width - block_size)) / block_size) * block_size
apple_y = round((random.randrange(0, display_height - block_size)) / block_size) * block_size
v_flag = 0
h_flag = 0 
snakelist = []
snakelen = 0


while not game_exit:
	#start
	while game_over:
		lead_x, lead_y = round((display_width / 2) / block_size) * block_size, round((display_height / 2) / block_size) * block_size
		snakelist = [] #[[0,10],[0,20],[0,30],[0,40],[0,50],[0,60],[0,70],[0,80],[0,90],[0,100],[0,110],[0,120],[0,130],[0,140],[0,150],[0,160],[0,170]]
		snake_head = [lead_x, lead_y]
		snakelist.append(snake_head)
		snakelen = 1

		#screen display
		game_display.fill(white)

		message_to_screen("Slither!", 20, 20, 50, dark_green)
		message_to_screen("Press any key to play", 30, 60, 25, green)
		
		#event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				game_over = False

		pygame.display.update()
	
	#event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_exit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if not v_flag:
					lead_x_change = 0
					lead_y_change = -block_size
					v_flag = 1
					h_flag = 0
			elif event.key == pygame.K_LEFT:
				if not h_flag:
					lead_x_change = -block_size
					lead_y_change = 0
					v_flag = 0
					h_flag = 1	
			elif event.key == pygame.K_DOWN:
				if not v_flag:
					lead_x_change = 0
					lead_y_change = block_size
					v_flag = 1
					h_flag = 0
			elif event.key == pygame.K_RIGHT:
				if not h_flag:
					lead_x_change = block_size
					lead_y_change = 0
					v_flag = 0
					h_flag = 1
	
	#movement
	lead_x += lead_x_change
	lead_y += lead_y_change	
	
	if (lead_x > (display_width - block_size)) or (lead_x < 0) or (lead_y > (display_height - block_size)) or (lead_y < 0):
		game_over = True
	
	for i in range(0, len(snakelist)):
		for j in range(i + 1, len(snakelist)):
			if snakelist[i][0] == snakelist[j][0] and snakelist[i][1] == snakelist[j][1]:
				game_over = True 
	
	if lead_x == apple_x and lead_y == apple_y:
		apple_x = round((random.randrange(0, display_width - block_size)) / block_size) * block_size
		apple_y = round((random.randrange(0, display_height - block_size)) / block_size) * block_size
		snakelen += 1

	#backgroud is white
	game_display.fill(white)
	
	snake_head = [lead_x, lead_y]
	snakelist.append(snake_head)
	snake(snakelist, snakelen)

	apple(apple_x, apple_y)

	#display update
	clock.tick(FPS)
	pygame.display.update()

pygame.quit()
quit()

