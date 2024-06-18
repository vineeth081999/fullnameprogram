nums=[23,45,67,91,84,58]
cinema=['departed','vikram','godfellas','usual suspects']
mixed=[2.0,12,'interstellar',67,'batman']
print(nums);
print(cinema);
print(mixed);
nums.append(100);
cinema.append('Dune');
mixed.append(3.5);
print(nums);
print(cinema);
print(mixed);
nums.insert(4,99);
cinema.insert(3,'Salaar');
mixed.insert(5,4.5);
print(nums);
print(cinema);
print(mixed);
nums.remove(100);
cinema.remove('Salaar');
mixed.remove(3.5);
print(nums);
print(cinema);
print(mixed);
nums.pop(3);
cinema.pop(2);
mixed.pop(5);
print(nums);
print(cinema);
print(mixed);
del nums[3:];
del cinema[2:];
del mixed[1:];
print(nums);
print(cinema);
print(mixed);
nums[2]=100;
cinema[1]='Dune part 2';
print(nums);
print(cinema);
cinema.extend(['Inception','kill bill']);
print(cinema);

