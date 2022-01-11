import random


def spider_web(web_map, starting, ending):
    done = web_map
    current_pos = starting
    final_list = spider_web_rec(web_map, current_pos, ending, done)
    if len(final_list) == 1:
        print([])
    else:
        print(final_list)




def spider_web_rec(web_map, starting, ending, visited):
    travel = []
    travel.append(starting)
    count = 0
    #runs through map and marks if visited
    for i in web_map:
        for j in range(len(web_map[i])):
            if web_map[i][j] == starting:
                web_map[i][j] = 'visited'
    #runs while the number of times run is less than the amount visited.
    while count < len(web_map[starting]):
        if starting == ending:
            return travel
        elif 'Node' in web_map[starting][count]:
            starting = web_map[starting][count]
            travel.append(spider_web_rec(web_map, starting, ending, visited))
        count += 1
    return travel


def make_spider_web(num_nodes, seed=0):
    if seed:
        random.seed(seed)

    web_map = {}

    for i in range(1, num_nodes + 1):
        web_map[f'Node {i}'] = []

    for i in range(1, num_nodes + 1):
        sample = random.sample(list(range(i, num_nodes + 1)), random.randint(1, num_nodes - i + 1))
        print('sample', i, sample)
        for x in sample:
            if i != x:
                web_map[f'Node {i}'].append(f'Node {x}')
                web_map[f'Node {x}'].append(f'Node {i}')
    return web_map


if __name__ == '__main__':
    num_nodes, seed = [int(x) for x in input('Input num_nodes, seed: ').split(',')]
    the_web = make_spider_web(num_nodes, seed)
    spider_web(the_web, 'Node 1', f'Node {num_nodes}')
