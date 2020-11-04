from rest_framework import serializers
from CitasMedicas.models import Persona, Consultorio, Estado

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('cod_per',
                  'nom_per',
                  'fna_per',
                  'dir_per',
                  'ema_per',
                  'usu_per',
                  'pas_per')

class ConsultorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultorio
        fields = ('cod_con',
                  'des_con')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('cod_est',
                  'des_est')