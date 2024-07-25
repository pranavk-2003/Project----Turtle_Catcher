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

To set up Turtle Catcher on your local machine, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/pranavk-2003/turtle_catcher.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd turtle_catcher
   ```

3. **Install ROS2 Humble and turtlesim:**
   Follow the [ROS2 Humble installation guide](https://docs.ros.org/en/humble/Installation.html) to install ROS2 Humble on your system.
   Once ROS2 Humble is installed, install the turtlesim package:
   ```sh
   sudo apt-get install ros-humble-turtlesim
   ```

4. **Build the project:**
   ```sh
   colcon build
   ```

5. **Source the setup file:**
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

---

Feel free to customize this template further according to your project's specific details.
