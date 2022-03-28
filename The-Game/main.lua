
local bx, by = 0, 0

function love.draw()
  bkg = love.graphics.newImage("assets/levelAssets/bkg.jpg")
  love.graphics.circle("fill", bx, by, 20)
end

function love.touchmoved(id, x, y, dx, dy, pressure)
  bx = x
  by = y
end

