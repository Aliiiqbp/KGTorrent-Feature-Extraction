import pandas as pd

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)


# f = pd.read_csv('code_batch_the_final.csv')
# g = f[['project_name', 'project_ID', 'cell_index', 'source', 'output_type', 'execution_count']]
# g.to_csv('code_batch_the_final_no_output.csv')
# lineterminator='\n'

df_final = pd.DataFrame(columns=['project_name', 'project_ID', 'cell_index', 'source'])

for i in range(1, 50):
    print('##########__' + str(i) + '__##########')
    f = pd.read_csv('2.markdown_batches/markdown_batch_' + str(i) + '.csv')
    df_final = pd.concat([df_final, f], ignore_index=True, axis=0)
    del f

f = pd.read_csv('2.markdown_batches/markdown_batch_the_final.csv')
df_final = pd.concat([df_final, f], ignore_index=True, axis=0)
df_final.to_csv('final_markdown.csv')
# f = pd.read_csv('2.markdown_batches/markdown_batch_' + str(24) + '.csv')
# print(f)
