const net = require('net');

const server = net.createServer(socket => {
    console.log('Client connected');

    socket.on('data', data => {
        console.log('Received data from client:', data.toString());
        // // Send the received data to the connected clients
        // broadcast(data.toString());
    });

    socket.on('end', () => {
        console.log('Client disconnected');
    });
});

server.listen(2000, () => {
    console.log('TCP server is listening on port 2000');
});

// Function to broadcast data to all connected clients
function broadcast(data) {
    // Here you can implement the logic to broadcast the data to your HTML page
    console.log('Broadcasting data:', data);
    // For example, you can emit a WebSocket event if you are using WebSocket
}
