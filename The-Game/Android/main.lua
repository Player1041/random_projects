function love.load()
    Object = require "lib.classic"
    require "codeAssets.player.player"
    
    safeX, safeY, safeW, safeH = love.window.getSafeArea()
    
    playericon = love.graphics.newImage("spriteAssets/player/player.png")
    r1 = player()
end

function love.draw()
    love.graphics.print(safeX, 100, 100)
    love.graphics.print(safeY, 100, 150)
    love.graphics.draw(playericon, 200, 100, 0, 2, 2)
    playericon:setFilter("nearest", "nearest")
end