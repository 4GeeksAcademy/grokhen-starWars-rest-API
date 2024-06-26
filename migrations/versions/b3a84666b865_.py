"""empty message

Revision ID: b3a84666b865
Revises: 9cf747ba4821
Create Date: 2024-06-06 16:06:23.787563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3a84666b865'
down_revision = '9cf747ba4821'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite_character', schema=None) as batch_op:
        batch_op.drop_constraint('favorite_character_user_id_key', type_='unique')

    with op.batch_alter_table('favorite_planet', schema=None) as batch_op:
        batch_op.drop_constraint('favorite_planet_user_id_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite_planet', schema=None) as batch_op:
        batch_op.create_unique_constraint('favorite_planet_user_id_key', ['user_id'])

    with op.batch_alter_table('favorite_character', schema=None) as batch_op:
        batch_op.create_unique_constraint('favorite_character_user_id_key', ['user_id'])

    # ### end Alembic commands ###
