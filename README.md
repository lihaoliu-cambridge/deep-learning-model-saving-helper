# Deep Learning Model-Saving Helper

Deep Learning Model-Saving Helper is a simple python framework which allows you to save your deep learning model's middle parameters (for visualization), deep learning model, and config file automatically without explicitly changing your code.


## Introduction

For deep learning researcher, a proposed model usually need many experiments with different parameters. The process of recording the parameters need explicit code modification. 

For example, changing you code from 
    ```sh
    tensorboard_log_dir = "~/log/test_1"
    batch_size = 32
    learning_rate = 1e-3
    ```
to
    ```sh
    tensorboard_log_dir = "~/log/test_2"
    batch_size = 40
    learning_rate = 1e-4
    ```

The above manually changing method is time-wasting and error-prone.

Our framework is mainly focused on solving the problem and it allows you to arrange your experiment's results in a more convenient way.


## Advantage

  - Automatically increasing the experiment number in the dir name, once you define the path and dir name in the config file. 

    E.g. you can define your middle results path(tensorboard_dir), model results(model_dir), note path(note_dir) in [args.yaml](https://github.com/CaptainWilliam/Deep-Learning-Model-Saving-Helper/blob/master/conf/args.yaml) in a yaml format.
    
    ```sh
    log_dir_params:
        tensorboard_dir: "./logs/tf_logs/resnet/log4tensorboard"
        model_dir: "./logs/tf_logs/resnet/log4model"
        note_dir: "./logs/tf_logs/resnet/note"
        self_increasing_mode: True       # False for overwriting the last dir
        pattern: "experiment"            # The dir name you want to use
        default_pattern: "defalut_name"
    ```
    
  - Help you to manage your model's parameters and pass them to your model easily.
 
    E.g. you can define your parameters in [args.yaml](https://github.com/CaptainWilliam/Deep-Learning-Model-Saving-Helper/blob/master/conf/args.yaml) file under the "running_params" item.
    
    ```sh
    running_params:
        batch_size: 64
        gpu_num: 1
        classes_num: 2
        
        conv_weight_decay: 0.0001
        bn_is_training: True
        bn_decay: 0.997
        bn_epsilon: 1e-5
        bn_scale: Truei
    
        learning_rate: 1e-3
        decay_steps: 1000
        decay_rate: 0.7
    ```
    
  - Copy the [args.yaml](https://github.com/CaptainWilliam/Deep-Learning-Model-Saving-Helper/blob/master/conf/args.yaml) file (which contains and manages you model's parameters) to the note path every time you run the program. If you wanna overwrite the last dir, change the self_increasing_mode item to "False".
    
    ![image](https://github.com/CaptainWilliam/StrawHat/blob/master/readme_pics/1.png)
    ![image](https://github.com/CaptainWilliam/StrawHat/blob/master/readme_pics/2.png)
    ![image](https://github.com/CaptainWilliam/StrawHat/blob/master/readme_pics/3.png)


## Installation

Your don't need tensorflow or other deep learning framework to run.

Download and unzip Deep-Learning-Model-Saving-Helper-master.zip

    ```sh
    $ cd Deep-Learning-Model-Saving-Helper-master
    $ python main.py
    ```

## Running

 - Modify the [args.yaml](https://github.com/CaptainWilliam/Deep-Learning-Model-Saving-Helper/blob/master/conf/args.yaml), add the parameters your deep learning model need under the "running_params" item .
 - Pass the running_params (a python dict which contains the running parameters) to you own model.
 - Finish you model, and run it.
 
 
## Question

Please open an issue or email 'lhliu1994@gmail.com' for any question.

