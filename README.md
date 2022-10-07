# DoSPy 

DoSPy, a script to *execute DoS* (Denial of Service) attacks on a specific host, allowing to define the amount of data sent and threads.

The greater the number of data sent, the *greater chance* the host will go down. We tested with 100 threads and a 50,000 byte token being sent to the router, the **traffic was congested** and no one could connect to the Wi-Fi network.

> **We are NOT responsible** for attacks made on servers, the script created is for teaching and learning purposes!

## How to use

To get started, clone the official repository into a directory. Then, enter the project root and run the command below:

```
python3 dospy-run.py
```

This will launch the interactive interface in the console, from there you can use `DoSPy`.

## License

```
GNU General Public License v3.0
```

This software uses the `GPL v3.0` license, for more information, [see LICENSE file](https://github.com/jaedsonpys/dospy/blob/master/LICENSE).