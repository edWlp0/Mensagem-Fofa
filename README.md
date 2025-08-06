import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("=== CALCULADORA SIMPLES ===");

        System.out.print("Digite o primeiro número: ");
        double num1 = input.nextDouble();

        System.out.print("Digite o operador (+, -, *, /): ");
        char operador = input.next().charAt(0);

        System.out.print("Digite o segundo número: ");
        double num2 = input.nextDouble();

        double resultado = 0;
        boolean valido = true;

        switch (operador) {
            case '+':
                resultado = num1 + num2;
                break;
            case '-':
                resultado = num1 - num2;
                break;
            case '*':
                resultado = num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    resultado = num1 / num2;
                } else {
                    System.out.println("Erro: divisão por zero.");
                    valido = false;
                }
                break;
            default:
                System.out.println("Operador inválido.");
                valido = false;
        }

        if (valido) {
            System.out.println("Resultado: " + resultado);
        }

        input.close();
    }
}
