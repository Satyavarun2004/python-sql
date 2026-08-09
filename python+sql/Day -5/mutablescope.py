global_var="hi"
def show():
    local_var="hello"
    print(global_var)
    print(local_var)

nums=[1,2,3,4,5]
print("original nums:",nums)
nums.append(6)
print("after append:",nums)

values=(1,2,3,4,5)
print("original values:",values)

print("list_slice:",nums[1:3])
print("tuple_slice:",values[:2])

print("\nVariable Scope")
show_scope()

