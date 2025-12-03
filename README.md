# Juego de Pelea de Samuráis

Este es un juego de pelea 2D desarrollado con **Pygame**, donde dos samuráis se enfrentan en un combate épico. El objetivo es demostrar habilidades en animaciones, manejo de entradas de usuario, barras de salud y movimiento de personajes, entregando un prototipo funcional con un diseño modular.

## Características
- **Animaciones fluidas**: Cada acción está animada, desde ataques hasta movimientos.
- **Controles precisos**: Respuesta rápida a las teclas para un gameplay dinámico.
- **Barras de salud**: Indicadores que reflejan el estado de cada jugador.
- **Selección de mapas**: Elige entre el mapa original con plataformas o el mapa plano para combates más intensos.
- **Diseño modular**: Código limpio y fácil de entender.

## Requisitos
- Python 3.8 o superior instalado en tu sistema.
- [uv](https://docs.astral.sh/uv/) (recomendado) o pip para gestionar dependencias.

## Instalación y Ejecución

### Con uv (Recomendado)
```bash
# Instalar uv si no lo tienes
curl -LsSf https://astral.sh/uv/install.sh | sh

# Ejecutar el juego
uv run python main.py
```

### Con pip
```bash
# Instalar dependencias
pip install pygame

# Ejecutar el juego
python main.py
```

## Controles

### Jugador 1
- **Movimiento**: ↑, ↓, ←, →
- **Defender**: O
- **Atacar**: P

### Jugador 2
- **Movimiento**: W, A, S, D
- **Defender**: G
- **Atacar**: H
