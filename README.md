# RT-Tools-RPi

Real-Time System: Tools & Kernel patches for patching the Rasbian kernel with RT-Preempt or Xenomai v3.0.7.

## Preempt-RT
You can find additional information reading these posts:
* [#Raspberry Pi: Real Time System - Preempt-RT Patching Tutorial for Kernel 4.14.y](https://lemariva.com/blog/2018/07/raspberry-pi-preempt-rt-patching-tutorial-for-kernel-4-14-y)
* [#Raspberry Pi: The N-queens Problem! (benchmark) Preempt-RT vs. Standard Kernel!](https://lemariva.com/blog/2018/04/raspberry-pi-the-n-queens-problem-performance-test)
* [#Rapberry Pi: Preempt-RT Kernel Performance on Rasbperry PI 3 Model B+](https://lemariva.com/blog/2018/04/rapberry-pi-preempt-rt-kernel-performance-on-rasbperry-pi-3-model-b)

## Xenomai v3.0.7
* [#Raspberry Pi: Real Time System - Xenomai Patching Tutorial for Kernel 4.14.y](https://lemariva.com/blog/2018/07/raspberry-pi-xenomai-patching-tutorial-for-kernel-4-14-y)

## Compiled Kernel Patches
* the folder `preempt-rt` includes the Preempt-RT patched kernels:
  * kernel_4_14_21-rt17-v7+	
  * kernel_4_14_27-rt21-v7+
  * kernel_4_14_52-rt34-v7+
* the folder `xenomai/v3.0.7` includes the patched kernel:
  * kernel_4_14_37-v7+
If you don't want to, you don't need to compile the kernel again: You can donwload these patches and deploy them. More info:
* [#Raspberry Pi: Real Time System - Preempt-RT Patching Tutorial for Kernel 4.14.y](https://lemariva.com/blog/2018/07/raspberry-pi-preempt-rt-patching-tutorial-for-kernel-4-14-y)
* [#Raspberry Pi: Real Time System - Xenomai Patching Tutorial for Kernel 4.14.y](https://lemariva.com/blog/2018/07/raspberry-pi-xenomai-patching-tutorial-for-kernel-4-14-y)

## References
Patches included in patches-backup are backup copies from:
* [usb-dwc_otg-fix](https://raw.githubusercontent.com/fedberry/kernel/master/usb-dwc_otg-fix-system-lockup-when-interrupts-are-threaded.patch)
* [patch-4.14.20-rt17.patch.gz](https://www.kernel.org/pub/linux/kernel/projects/rt/4.14/patch-4.14.20-rt17.patch.gz)
