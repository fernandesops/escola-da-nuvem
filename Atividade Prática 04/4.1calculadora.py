def calculadora():

    while True:
        try:

            num1_input = input("Digite o primeiro número: ")
            

            operacao = input("Digite a operação (+, -, *, /): ")
            

            num2_input = input("Digite o segundo número: ")


            
            num1 = float(num1_input)
            num2 = float(num2_input)

            resultado = 0.0


            
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':

                if num2 == 0:

                    raise ZeroDivisionError
                resultado = num1 / num2
            else:

                raise ValueError("Operação inválida")

            print(f"\nSucesso! O resultado é: {num1} {operacao} {num2} = {resultado}")
            

            break


        
        except ValueError as e:

            
            if 'Operação inválida' in str(e):

                print("\n[ERRO] Operação inválida. Por favor, use apenas '+', '-', '*' ou '/'.")
            else:

                print("\n[ERRO] Entrada numérica inválida. Por favor, digite apenas números.")
        
        except ZeroDivisionError:

            print("\n[ERRO] Impossível dividir por zero.")
        
        except Exception as e:
            print(f"\n[ERRO] Um erro inesperado ocorreu: {e}")

        print("Por favor, tente novamente.\n")



if __name__ == "__main__":
    calculadora()