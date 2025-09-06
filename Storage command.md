**RAM, swap, disk storage, and file sizes** 
on Jupyter ubeflow (same as Linux); you can use these commands:

---

### **1️⃣ Memory usage (RAM & swap)**

```bash
free -h
```

Output example:

```
               total        used        free      shared  buff/cache   available
Mem:            47Gi        19Gi       5.3Gi       129Mi        21Gi        26Gi
Swap:             0B          0B          0B
```

---

### **2️⃣ Disk usage (overall)**

```bash
df -h
```

Output example:

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       100G   60G   35G  64% /
```

---

### **3️⃣ Disk usage of a specific directory**

```bash
du -sh /path/to/directory
```

Example for your synthetic data folder:

```bash
du -sh /home/jovyan/vite-datavol-1/synthetic_data
```

Output example:

```
12G    /home/jovyan/vite-datavol-1/synthetic_data
```

---

### **4️⃣ List files with size**

```bash
ls -lh /home/jovyan/vite-datavol-1/synthetic_data
```

Output example:

```
-rw-r--r-- 1 jovyan jovyan 10M Sep 6 21:00 synthetic_000001.npy
-rw-r--r-- 1 jovyan jovyan 10M Sep 6 21:01 synthetic_000002.npy
```

---

### **5️⃣ Check a specific file size**

```bash
stat -c %s /home/jovyan/vite-datavol-1/synthetic_data/synthetic_000001.npy
```

Output in bytes:

```
10485760
```

---


