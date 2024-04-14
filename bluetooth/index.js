const ffi = require('ffi-napi');
const ref = require('ref-napi');

// Load the Bluetooth API library
const bluetooth = ffi.Library('Bthprops', {
    'BluetoothFindFirstDevice': ['pointer', ['pointer', 'pointer']],
    'BluetoothFindNextDevice': ['int', ['pointer', 'pointer']],
    'BluetoothFindDeviceClose': ['int', ['pointer']]
});

// Define the Bluetooth device information structure
const BLUETOOTH_DEVICE_INFO = ref.struct({
    dwSize: ref.types.uint32,
    Address: 'ulonglong',
    ulClassofDevice: 'uint32',
    fConnected: 'int',
    szName: 'string',
    ulFlags: 'uint32'
});

// Function to find Bluetooth devices
function findBluetoothDevices() {
    // Initialize the Bluetooth device info structure
    const deviceInfo = new BLUETOOTH_DEVICE_INFO();
    deviceInfo.dwSize = BLUETOOTH_DEVICE_INFO.size;

    // Find the first Bluetooth device
    const hDevice = bluetooth.BluetoothFindFirstDevice(deviceInfo.ref(), null);

    if (hDevice.isNull()) {
        console.error('No Bluetooth devices found.');
        return;
    }

    console.log('Bluetooth Devices:');

    do {
        console.log(deviceInfo.szName);
    } while (bluetooth.BluetoothFindNextDevice(hDevice, deviceInfo.ref()));

    bluetooth.BluetoothFindDeviceClose(hDevice);
}

// Call the function to find Bluetooth devices
findBluetoothDevices();
