================================================================================

Summary
	在這個程式中，一開始會出現蛇頭、白色的牆壁、綠色的毒藥、紅色的食物，而蛇頭的部分我則是設定為藍色，接下來加入的身體則會是黃藍相間，
	牆壁在生長時會和現有的牆壁接觸，並且沿著同一個方向生長，在這個程式裡可以使用上、下、左、右鍵控制蛇的移動去吃毒藥或是食物，當吃到食物時，
	身體會加長一格，而吃到毒藥時，則會減短一格，最後當蛇碰到自己或是超出範圍時，遊戲結束。
	
================================================================================

移動
	玩家移動(Model.py Player.move)
		在移動的部分，先判斷其移動方向後，加入一個新的頭在第0個位子，並且把蛇身的最後一節刪除的方式讓它移動

================================================================================

生成物件
	生成牆壁 (Controller.py generate_wall)、新牆壁生在現有牆壁周圍
		一開始先隨機生成一座標後，接著去檢查是否和蛇(蛇頭 + 蛇身)碰到或是和牆壁碰到
		如果碰到，就重新產生一個
		如果沒有碰到，就加入list裡面
		如果已經有牆壁，direction為上或下時，要sort_by_y找出最上方或最下方的座標，然和在它的上方或下方加入一個新的牆
			     direction為左右時，sort_by_x找出最左或最右的座標，然後在他的左方或右方加入一個牆壁
		最後在程式的最後return direction就能讓他朝著同一個方向作生長

	生成食物 (Controller.py generate_food)
		也是先隨機生成後，再判斷是不是有碰到牆或是蛇
		碰到就重新生成一個
		沒有就將他加入list

	生成毒藥 (Controller.py generate_poison)
		隨機生成一個毒物後，判斷是否和牆壁、食物、或蛇碰到
		碰到就重新生成一個
		沒有就將他加入list
		
	生成蛇(Model.py Player.new_block)
		使用append將新的一節加入
		
		
================================================================================

碰撞
	邊界碰撞(Player.check_border)
		如果蛇頭的x座標小於0或蛇頭x座標加上一格SNAKE_SIZE得到的座標大於螢幕寬
		或是蛇頭的y座標小於0或蛇頭y座標加上一格SNAKE_SIZE得到的座標大於螢幕的高則會超出螢幕範圍

	蛇碰撞(Player.detect_player_collision)
		使用for來將身體裡的每一節取出，如果蛇頭和身體的座標相減小於一節身體的長就會碰到
		如果沒有碰到則一直執行到碰到或是比較完整隻蛇的每一節

	牆壁碰撞(Player.detect_wall_collision)
		牆壁的碰撞和蛇碰撞使用了相同的寫法
		使用for來將每一節牆壁取出，如果蛇頭和身體的座標相減小於一節身體的長就會碰到
		如果沒有碰到則一直執行到碰到或是比較完整個牆壁的list

	食物碰撞(Player.detect_food_collision)
		食物碰撞的寫法也和蛇碰撞以及牆壁碰撞一樣
		使用for來將每一節牆壁取出，如果蛇頭和身體的座標相減小於一節身體的長就會碰到
		如果沒有碰到則一直執行到碰到或是比較完整個食物的list
		
================================================================================

遊戲機制
	根據蛇長度調整移動間格(Controller.py 的 calculate_time_interval)
		依據蛇的長度的不同，速度會有所不同
		蛇的長度每增加四幀移動頻率就加一，而移動頻率最大值為10，最小為5

================================================================================

其他
	畫蛇添足(Player.draw_snake)
		設定一開始為藍色
		接下來黃藍相間

	顏色
		我把原先設定蛇的藍色(0, 0, 200)換為淺藍色(64, 140, 244)
		黃色(200, 200, 60)則換為淺黃色(255, 255, 170)
