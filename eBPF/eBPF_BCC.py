from  pyebpf import ebpf_wrapper

b = ebpf_wrapper.EBPFWrapper()
# b.attach_kprobe()
print(b.attach_kprobe())