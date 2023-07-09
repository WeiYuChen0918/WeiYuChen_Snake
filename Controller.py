from typing import List
import pygame as pg
from Config import *
from Model import *
# ======== start ========

import random

# ======== end ========

def key_input(pressed_keys: List):
    """
    從 pygame 的鍵盤輸入判斷哪些按鍵被按下
    回傳方向
    """
    for key in pressed_keys:
        if key == pg.K_UP:
            movement = UP
            break
        if key == pg.K_DOWN:
            movement = DOWN
            break
        if key == pg.K_LEFT:
            movement = LEFT
            break
        if key == pg.K_RIGHT:
            movement = RIGHT
            break
        if key == pg.K_a:
            return "new"
    else:
        return None
    return movement

# 以下為大作業

# ======== start ========

def wall_sort_by_x(wall):
    return wall.pos_x

def wall_sort_by_y(wall):
    return wall.pos_y

# ======== end ========


def generate_wall(walls: List[Wall], player: Player, direction: int) -> None:
    """
    生成一個 `Wall` 的物件並加到 `walls` 裡面，不能與現有牆壁或玩家重疊
    新牆壁一定要與現有牆壁有接觸 (第一階段)，更好的話請讓牆壁朝著同個方向生長 (第二階段)
    無回傳值

    Keyword arguments:
    walls -- 牆壁物件的 list
    player -- 玩家物件
    direction -- 蛇的移動方向
    """
    # ======== start ========

    gen_first = 1
    gen_again = 0

    while (gen_first == 1 or gen_again == 1):
        gen_first = 0
        gen_again = 0

        if len(walls) == 0:
            x = random.randint(0, SCREEN_WIDTH - SNAKE_SIZE)
            y = random.randint(0, SCREEN_HEIGHT - SNAKE_SIZE)
        
            if gen_again == 0:
                for i in player.snake_list:
                    obj_x = i[0]
                    obj_y = i[1]

                    diff_x = abs(x - obj_x) # 取絕對值
                    diff_y = abs(y - obj_y)

                    if (diff_x < SNAKE_SIZE) and (diff_y < SNAKE_SIZE):
                        gen_again = 1
                        break
                    else:
                        gen_again = 0
                        continue
        else:
            if direction == LEFT:
                walls.sort(key=wall_sort_by_x)
                x = walls[0].pos_x - SNAKE_SIZE
                y = walls[0].pos_y

            elif direction == RIGHT:
                walls.sort(key=wall_sort_by_x)
                x = walls[-1].pos_x + SNAKE_SIZE
                y = walls[-1].pos_y

            elif direction == UP:
                walls.sort(key=wall_sort_by_y)
                x = walls[0].pos_x 
                y = walls[0].pos_y - SNAKE_SIZE 

            elif direction == DOWN:
                walls.sort(key=wall_sort_by_y)
                x = walls[-1].pos_x 
                y = walls[-1].pos_y + SNAKE_SIZE

    new_wall = Wall([x, y])
    walls.append(new_wall)                                      
    
    return direction
    # ======== end ========    
        

def generate_food(foods: List[Food], walls: List[Wall], player: Player) -> None:
  
    """
    在隨機位置生成一個 `Food` 的物件並加到 `foods` 裡面，不能與現有牆壁或玩家重疊
    無回傳值

    Keyword arguments:
    foods -- 食物物件的 list
    walls -- 牆壁物件的 list
    player -- 玩家物件S
    """
    # ======== start ========

    gen_first = 1
    gen_again = 0

    while (gen_first == 1 or gen_again == 1):
        gen_first = 0
        gen_again = 0

        x = random.randint(0, SCREEN_WIDTH - SNAKE_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - SNAKE_SIZE)

        if gen_again == 0:
            for i in player.snake_list:
                obj_x = i[0]
                obj_y = i[1]

                diff_x = abs(x - obj_x) # 取絕對值
                diff_y = abs(y - obj_y)

                if (diff_x < SNAKE_SIZE) and (diff_y < SNAKE_SIZE):
                    gen_again = 1
                    break
                else:
                    gen_again = 0
                    continue

        if gen_again == 0:
            for i in walls:
                obj_x = i.pos_x
                obj_y = i.pos_y

                diff_x = abs(x - obj_x) # 取絕對值
                diff_y = abs(y - obj_y)

                if (diff_x < SNAKE_SIZE) and (diff_y < SNAKE_SIZE):
                    gen_again = 1
                    break
                else:
                    gen_again = 0
                    continue

        if gen_again == 0:
            for i in foods:
                obj_x = i.pos_x
                obj_y = i.pos_y

                diff_x = abs(x - obj_x) # 取絕對值
                diff_y = abs(y - obj_y)

                if (diff_x < SNAKE_SIZE) and (diff_y < SNAKE_SIZE):
                    gen_again = 1
                    break
                else:
                    gen_again = 0
                    continue 
    
    new_food = Food([x, y])
    foods.append(new_food)
    
    return

    # ======== end ========
   
    


def generate_poison(walls: List[Wall], foods: List[Food], player: Player) -> None:
    """
    在隨機位置生成一個 `Poison` 的物件並回傳，不能與現有其他物件或玩家重疊
    有回傳值

    Keyword arguments:
    walls -- 牆壁物件的 list
    foods -- 食物物件的 list
    player -- 玩家物件
    """
    # ======== start ========
    
    gen_first = 1
    gen_again = 0

    while (gen_first == 1 or gen_again == 1):
        gen_first = 0
        gen_again = 0

        x = random.randint(0, SCREEN_WIDTH - SNAKE_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - SNAKE_SIZE)

        if gen_again == 0:
            for i in player.snake_list:
                obj_x = i[0]
                obj_y = i[1]

                diff_x = abs(x - obj_x) # 取絕對值
                diff_y = abs(y - obj_y)

                if (diff_x < SNAKE_SIZE) and (diff_y < SNAKE_SIZE):
                    gen_again = 1
                    break
                else:
                    gen_again = 0
                    continue

        if gen_again == 0:
            for i in walls:
                obj_x = i.pos_x
                obj_y = i.pos_y

                diff_x = abs(x - obj_x) # 取絕對值
                diff_y = abs(y - obj_y)

                if (diff_x < SNAKE_SIZE) and (diff_y < SNAKE_SIZE):
                    gen_again = 1
                    break
                else:
                    gen_again = 0
                    continue

        if gen_again == 0:
            for i in foods:
                obj_x = i.pos_x
                obj_y = i.pos_y

                diff_x = abs(x - obj_x) # 取絕對值
                diff_y = abs(y - obj_y)

                if (diff_x < SNAKE_SIZE) and (diff_y < SNAKE_SIZE):
                    gen_again = 1
                    break
                else:
                    gen_again = 0
                    continue 
    
    new_poison = Poison([x, y])
    
    return new_poison

    # ======= end ========           



def calculate_time_interval(player: Player) -> int:
    """
    根據蛇的長度，計算並回傳每一秒有幾幀
    蛇的長度每增加 4 幀數就 +1，從小到大，最大為 `TIME_INTERVAL_MAX`，最小為 `TIME_INTERVAL_MIN`
    """
    # ======== start ========

    frame_rate = TIME_INTERVAL_MIN + int(player.length / 4)
    if frame_rate > TIME_INTERVAL_MAX:
        frame_rate = TIME_INTERVAL_MAX

    return frame_rate
    
    # ======== end ========

