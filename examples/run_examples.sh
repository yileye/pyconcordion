export PYTHONPATH=./src
python -t src/scripts/concordion_runner -e org.concordion.ext.Extensions ./examples
python -t src/scripts/concordion_runner -e org.concordion.ext.Extensions ./concordion_run_example/indexTest
