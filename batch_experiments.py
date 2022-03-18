from distutils import command
import os
import wandb


args_dict = {'env':'groups_simple_stationary-v0', 
'model':'paper_txt2pi',
'demb':'30',
'drnn_small': '10',
'drnn':'100',
'drep':'400',
'num_actors':'20',
'batch_size':'24',
'learning_rate':'0.0007',
'total_frames':'10000',
'height':'6',
'width':'6'}


#this particular experiment looks at learning rate
for i in range(1,2):
    args_dict['learning_rate'] = str(0.0007 * i * 2)
    wandb.config = args_dict
    command_string = "python run_exp.py "

    for k, v in args_dict.items():
        command_string += '--' + k + " " + v + " "

    os.system(command_string)


'''command_string = "python run_exp.py "
for k, v in args_dict.items():
    command_string += '--' + k + " " + v + " "
os.system(command_string)'''