{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOHejqi0PuS4DX5aaSEVc0P",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Msevero-tech/gestor-de-gastos-py/blob/main/gestor_Gastos_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xGLin1K1Ymk7",
        "outputId": "d2212d03-8374-4d9a-828b-46a5c081e479"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ingresa tu nombre: Marcos\n",
            "Bienvenido Marcos te voy a ayudar para organizar tus gastos\n",
            "ingresa tu presupuesto: 400000\n",
            "Gestor de gastos\n",
            "¿Cuántos gastos querés ingresar? 4\n",
            "Ingresá un gasto: 150000\n",
            "Ingresá un gasto: 50000\n",
            "Ingresá un gasto: 120000\n",
            "Ingresá un gasto: 80000\n",
            "Estas en 0 gastaste todo te presupuesto\n",
            "Usaste el 100.0 % de tu presupuesto\n",
            "\n",
            "RESULTADOS\n",
            "Total gastado: 400000.0\n",
            "Promedio: 100000.0\n",
            "Gasto más alto: 150000.0\n",
            "Gasto mas bajo: 50000.0\n"
          ]
        }
      ],
      "source": [
        "gastos = []\n",
        "\n",
        "nombre = input(\"ingresa tu nombre: \")\n",
        "\n",
        "print(\"Bienvenido\", nombre, \"te voy a ayudar para organizar tus gastos\")\n",
        "\n",
        "presupuesto = float(input(\"ingresa tu presupuesto: \"))\n",
        "\n",
        "print(\"Gestor de gastos\")\n",
        "\n",
        "cantidad = int(input(\"¿Cuántos gastos querés ingresar? \"))\n",
        "\n",
        "for i in range(cantidad):\n",
        "    gasto = float(input(\"Ingresá un gasto: \"))\n",
        "    gastos.append(gasto)\n",
        "\n",
        "total = sum(gastos)\n",
        "promedio = total / cantidad\n",
        "mayor = max(gastos)\n",
        "\n",
        "restante = presupuesto - total\n",
        "\n",
        "if total > 5000000:\n",
        "   print(\"El gasto es muy alto\")\n",
        "\n",
        "if total > presupuesto:\n",
        "   print(\"Te pasaste de tu presupuesto\")\n",
        "elif total == presupuesto:\n",
        "   print(\"Estas en 0, gastaste todo te presupuesto\")\n",
        "else:\n",
        "   print(\"Muy bien\", nombre, \"te quedan\", restante, \"para gastar\")\n",
        "\n",
        "porcentaje = (total / presupuesto) * 100\n",
        "print(\"Usaste el\", round(porcentaje,2), \"% de tu presupuesto\")\n",
        "\n",
        "print(\"\\nRESULTADOS\")\n",
        "print(\"Total gastado:\", total)\n",
        "print(\"Promedio:\", promedio)\n",
        "print(\"Gasto más alto:\", mayor)\n",
        "print(\"Gasto mas bajo:\", min(gastos))"
      ]
    }
  ]
}
