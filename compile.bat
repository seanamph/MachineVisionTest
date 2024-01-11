del *.o
g++ -c NImage.cpp -o NImage.o
g++ -c NImageDLL.cpp -o NImageDLL.o
g++ -shared -o NImageDLL.dll *.o