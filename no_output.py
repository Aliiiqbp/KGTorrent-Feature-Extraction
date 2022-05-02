import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)


# f = pd.read_csv('code_batch_the_final.csv')
# g = f[['project_name', 'project_ID', 'cell_index', 'source', 'output_type', 'execution_count']]
# g.to_csv('code_batch_the_final_no_output.csv')

for i in range(24, 25):
    print('##########__' + str(i) + '__##########')
    f = pd.read_csv('code_batch_' + str(i) + '.csv', lineterminator='\n')
    g = f[['project_name', 'project_ID', 'cell_index', 'source', 'output_type', 'execution_count']]
    g.to_csv('code_batch_' + str(i) + '_no_output.csv')
    del f
