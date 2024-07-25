
# Turtle Catcher




## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Turtle Catcher is a project developed using ROS2 Humble and the turtlesim package. The project involves a turtle that automatically navigates to catch other turtles that spawn randomly in the simulation environment.

## Features

- Autonomous turtle navigation
- Random turtle spawning
- Service-based turtle catching and killing
- ROS2 and turtlesim integration
- Real-time display of alive turtles

## Installation

To set up Turtle Catcher, follow these steps:

1. **Create a ROS2 workspace:**
   ```sh
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws
   ```

2. **Clone the `turtle_catcher` repository and move the `src` directory:**
   ```sh
   git clone --depth 1 https://github.com/pranavk-2003/turtle_catcher.git
   mv turtle_catcher/src ~/ros2_ws/src/
   rm -rf turtle_catcher
   ```

3. **Build the workspace:**
   ```sh
   colcon build
   ```

4. **Source the setup file:**
   ```sh
   source install/setup.bash
   ```

## Usage

To run the Turtle Catcher project, use the provided launch file:

```sh
ros2 launch my_robot_bringup turtle_catcher.launch.py
```

This will start the turtlesim node, the turtle spawner node, and the turtle controller node all at once. The turtle will automatically navigate to catch the spawned turtles.

## Contributing

We welcome contributions to improve Turtle Catcher! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Create a pull request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
