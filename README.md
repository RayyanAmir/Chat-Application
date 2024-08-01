## Project Overview

**Multi-User Client-Server Chat Application**

This project is a Python-based multi-user client-server chat application. It enables multiple users to connect to a central server, create groups, and chat in real-time. The server listens for incoming client connections, and clients must input the server's IP address to join. An admin has the authority to manage users, including banning disruptive users.

## Features

1. **Real-time Messaging**
   - Users can send and receive messages in real-time.

2. **Group Chat**
   - Users can create and join groups for collective discussions.

3. **Admin Controls**
   - The admin can manage the chat environment, including banning users.

4. **Server Configuration**
   - Clients can connect to the server by inputting its IP address.

## Files

- **server.py**
  - Contains the server-side code for managing client connections and facilitating message exchanges.

- **client.py**
  - Contains the client-side code for connecting to the server and interacting with other users.

- **servers.json**
  - Configuration file that includes example server details for ease of connection.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Basic understanding of socket programming.

### Running the Application

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/multi-user-chat-application.git
2.  **Usage:**
- Starting a Chat Session: Once connected, clients can start sending messages that will be broadcast to all connected users.
- Creating Groups: Users can create groups to organize discussions.
Admin Controls: The admin can issue commands to manage users, including banning those who violate chat rules.
3. **Future Enhancements**
- User Authentication: Implement user login and registration.
- Private Messaging: Allow users to send private messages.
- Enhanced Admin Controls: More robust user management features.
4.**Contribution**
- Feel free to contribute to the project by submitting issues and pull requests. Follow the standard GitHub contribution guidelines.

