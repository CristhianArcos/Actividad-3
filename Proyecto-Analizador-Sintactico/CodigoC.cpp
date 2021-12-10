//#Textos
puts "Hola, mundo!"
puts ""
puts "Me gusta" + "el pastel de manzana."
puts "Mi IP es: 192.168.9.10"
puts "ragustin726@gmail.com"
puts "https://www.facebook.com"

//#Variables
myString = '...puedes decir eso de nuevo...'
puts myString
name = 'Patricia Rosanna Jessica Mildred Oppenheimer'
ID= 10.0.0.1
correo='roberto_840@hotmail.com'
direccion='https://www.google.com'
fecha = '19/07/2001'

//#Concatenaciones
puts 'Me llamo ' + name + '.'
puts 'Wow!  "' + name + '" es un nombre realmente largo!'
composer1 = 'Mozart'
puts composer1 + ' fue "el amo", en su día.'
composer = 'Beethoven'
puts 'Pero yo prefiero a ' + composer1 + ', personalmente.'


//#Condicionales
puts 1.7 > 2
puts 1 < 2
puts 5 >= 5
puts 5 <= 4
puts 1 == 1
puts 2 != 1
puts 'gato' < 'perro'

//#Asignacion de ID

Ingrese ID = "1568749"
puts "Su ID es " + ID +"."

///#Operaciones basicas.

using namespace std;

int opcion;

float primero=1;

float segundo=1;

float resultado;



int main(){



cout << "Que operacion desea realizar Suma [1] Resta [2] Multiplicacion [3] Division [4]." << endl;



cin >> opcion;

cout << "Ingrese un numero: ";

cin >> primero;

cout << "Ingrese un numero: ";

cin >> segundo;



if (opcion==1){

    resultado = primero+segundo;

}

if (opcion==2){

    resultado = primero-segundo;

}

if (opcion==3){

    resultado = primero*segundo;

}

if (opcion==4){

    resultado = primero/segundo;

}



cout << resultado;



cin.ignore();

cin.get(); 

return 0;

}