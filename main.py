import pygame
import sys

pygame.init()

window = pygame.display.set_mode([800, 580])

quadX = 100
quadY = 300
speedX = 0
speedY = 0

clock = pygame.time.Clock()
while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        speedX = -2
      if event.key == pygame.K_RIGHT:
        speedX = 2
      if event.key == pygame.K_UP:
        speedY = -2
      if event.key == pygame.K_DOWN:
        speedY = 2
    if event.type == pygame.KEYUP:
      if (event.key == pygame.K_LEFT
        or event.key == pygame.K_RIGHT):
          speedX = 0
      if (event.key == pygame.K_UP
        or event.key == pygame.K_DOWN):
          speedY = 0

  window.fill((200, 200, 200))

  pygame.draw.rect(
    window, (0, 0, 0), [0, 275, 800, 100]
  )

  pygame.draw.rect(
    window, (255, 255, 255), [quadX, quadY, 50, 50]
  )

  quadX += speedX
  quadY += speedY

  if quadY < 275 or quadY + 50 > 375:
    font = pygame.font.Font('freesansbold.ttf', 150)
    text = font.render('PERDEU', True, (255, 0, 0))
    window.blit(text, [100, 50])
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit()

  if quadX + 50 > 800:
    font = pygame.font.Font('freesansbold.ttf', 150)
    text = font.render('GANHOU', True, (50, 200, 50))
    window.blit(text, [50, 50])
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit()

  pygame.display.update()
  clock.tick(30)