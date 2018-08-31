def get_data_topo():
    #
    print 'kaishi'
    start=time.time()
    view={}
    view['rea_value'] = 0
    view['emu_value'] = 0
    view['sim_value'] = 0
    view['mms_value'] = 100000
    # node=view['node_num']+view['sim_num']+view['emu_num']+view['rea_num']
    if view['rea_value'] == 0 and view['emu_value'] == 0 and view['sim_value'] == 0 and view['mms_value'] == 0:
        node=1000
    node=836
    if int(math.sqrt(node/4)) % 2 == 0:
        n = int(math.sqrt(node/4))
    else:
        n = int(math.sqrt(node / 4)) + 1
    pos = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    r = 4
    d = 1
    count = 0
    node_id = 1
    nodes_list2 = []
    dict1 = {}


    for k in xrange(1, n):
        y = r * k
        if k == 1:
            for i in xrange(1, n):
                for j in xrange(1, n):
                    for s in xrange(len(pos)):
                        if i>=n-1 or j>=n-1:
                            continue
                        nodes_dict = {}
                        nodes_dict['site'] = [i * pos[s][0], y, j * pos[s][1]]
                        nodes_dict['node_category'] = ''
                        nodes_dict['node_type'] = 's'
                        nodes_dict['line'] = []
                        dict1[node_id] = nodes_dict
                        nodes_list2.append([i * pos[s][0], y, j * pos[s][1]])
                        count += 1
                        node_id += 1

        else:
            for i in xrange(1, n):
                for j in xrange(1, n):
                    for s in xrange(len(pos)):

                        # if (i>n-5 or j>n-5) and y==8:
                        #     break
                        nodes_list2.append([pos[s][0] * (d * (i - 0.5) + 0.5), y,
                                            (d * (j - 0.5) + 0.5) * pos[s][1]])
                        nodes_dict = {}
                        nodes_dict['site'] = [pos[s][0] * (d * (i - 0.5) + 0.5), y,
                                              (d * (j - 0.5) + 0.5) * pos[s][1]]

                        if y<=8:
                            q = [pos[s][0] * (d * (i - 0.5) + 0.5) - 0.5, y - 4,
                                 (d * (j - 0.5) + 0.5) * pos[s][1] - 0.5]
                            w = [pos[s][0] * (d * (i - 0.5) + 0.5) - 0.5, y - 4,
                                 (d * (j - 0.5) + 0.5) * pos[s][1] + 0.5]
                            e = [pos[s][0] * (d * (i - 0.5) + 0.5) + 0.5, y - 4,
                                 (d * (j - 0.5) + 0.5) * pos[s][1] - 0.5]
                            v = [pos[s][0] * (d * (i - 0.5) + 0.5) + 0.5, y - 4,
                                 (d * (j - 0.5) + 0.5) * pos[s][1] + 0.5]
                        else:
                            q=[pos[s][0] * (d * (i - 0.5) + 0.5) - d/4, y - 4,(d * (j - 0.5) + 0.5) * pos[s][1] - d/4]
                            w=[pos[s][0] * (d * (i - 0.5) + 0.5) - d/4, y - 4,
                                                                         (d * (j - 0.5) + 0.5) * pos[s][1] + d/4]
                            e=[pos[s][0] * (d * (i - 0.5) + 0.5) + d/4, y - 4,
                                                                         (d * (j - 0.5) + 0.5) * pos[s][1] - d/4]
                            v=[pos[s][0] * (d * (i - 0.5) + 0.5) + d/4, y - 4,
                                                                         (d * (j - 0.5) + 0.5) * pos[s][1] + d/4]
                        list_line=[]
                        try:
                            a=nodes_list2.index(q)
                            list_line.append(a + 1)
                            if y-4==4:
                                dict1[a + 1]['line'] = [node_id]
                            else:
                                dict1[a + 1]['line'].append(node_id)

                        except Exception as p:
                           pass
                        try:
                            s=nodes_list2.index(w)
                            list_line.append(s + 1)
                            if y - 4 == 4:
                                dict1[s + 1]['line'] = [node_id]
                            else:
                                dict1[s + 1]['line'].append(node_id)

                        except Exception as p:
                            pass
                        try:
                            f=nodes_list2.index(e)
                            list_line.append(f + 1)
                            if y - 4 == 4:
                                dict1[f + 1]['line'] = [node_id]
                            else:
                                dict1[f + 1]['line'].append(node_id)
                        except Exception as p:
                            pass
                        try:
                            m=nodes_list2.index(v)
                            list_line.append(m + 1)
                            if y - 4 == 4:
                                dict1[m + 1]['line'] = [node_id]
                            else:
                                dict1[m + 1]['line'].append(node_id)
                        except Exception as p:
                            pass
                        nodes_dict['line'] = list_line
                        nodes_dict['node_category'] = ''
                        nodes_dict['node_type'] = 's'
                        dict1[node_id] = nodes_dict
                        count += 1
                        node_id += 1


        n = int(n*0.5)
        d = d * 2
    print 'for' + str(time.time() - start)

    print 'kaishixieruwenjian'
    starts = time.time()
    with open('topology.json','w') as f:
        json.dump(dict1,f)
    print 'jieshu'+str(time.time()-starts)
    return count


get_data_topo()