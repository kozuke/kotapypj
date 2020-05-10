from click import option, command


@option('--start-num', '-sn', type=int)
@option('--end-num', '-en', type=int)
@option('--agg-unit', '-au', type=int)
@command()
def count_youtube(start_num, end_num, agg_unit):
    count_list = []
    for num in range(start_num, end_num + 1):
        count_list.append(num)

    out_list = []
    with open('out.csv', 'w') as f:
        for num in range(agg_unit):
            out_list.append(count_list[num::agg_unit])
            f.write(','.join(map(str, count_list[num::agg_unit])))
            f.write('\n')


if __name__ == '__main__':
    count_youtube()
