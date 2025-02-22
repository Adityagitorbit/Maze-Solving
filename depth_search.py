from pyMaze import maze,agent,COLOR

def depth_search(m):
    start = (m.rows, m.cols)
    explored = [start]
    stack = [start]
    def_path = {}
    
    while len(stack) > 0:
        current_cell = stack.pop()
        if current_cell == (1,1):
            break
        for d in 'EWNS':
            if m.maze_map[current_cell][d] == 1:
                if d == 'E':
                    child_cell = (current_cell[0], current_cell[1] + 1)
                elif d == 'W':
                    child_cell = (current_cell[0], current_cell[1] - 1)
                elif d == 'S':
                    child_cell = (current_cell[0] + 1, current_cell[1])
                elif d == 'N':
                    child_cell = (current_cell[0] - 1, current_cell[1])
                
                if child_cell in explored:
                    continue
                explored.append(child_cell)
                stack.append(child_cell)
                def_path[child_cell] = current_cell
    fdw = {}
    cell = (1,1)
    while cell != start:
        fdw[def_path[cell]] = cell
        cell = def_path[cell]
    return fdw



m  = maze(50,50)

m.CreateMaze(loopPercent= 100)

path = depth_search(m)
a = agent(m, footprints = True)
m.tracePath({a:path})

m.run()