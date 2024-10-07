"""empty message

Revision ID: 44184d6911f3
Revises: 7c760dc6d511
Create Date: 2024-09-19 08:04:18.393425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44184d6911f3'
down_revision = '7c760dc6d511'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Birth_year', sa.String(length=120), nullable=False),
    sa.Column('Eye_color', sa.String(length=120), nullable=False),
    sa.Column('Films', sa.String(length=120), nullable=False),
    sa.Column('Gender', sa.String(length=120), nullable=False),
    sa.Column('Hair_color', sa.String(length=120), nullable=False),
    sa.Column('Heigh', sa.String(length=120), nullable=False),
    sa.Column('Homeworld', sa.String(length=120), nullable=False),
    sa.Column('Mass', sa.String(length=120), nullable=False),
    sa.Column('Name', sa.String(length=120), nullable=False),
    sa.Column('Skin_color', sa.String(length=120), nullable=False),
    sa.Column('Created', sa.String(length=120), nullable=False),
    sa.Column('Edited', sa.String(length=120), nullable=False),
    sa.Column('Species', sa.String(length=120), nullable=False),
    sa.Column('Starships', sa.String(length=120), nullable=False),
    sa.Column('Url', sa.String(length=120), nullable=False),
    sa.Column('Vehicles', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Birth_year'),
    sa.UniqueConstraint('Created'),
    sa.UniqueConstraint('Edited'),
    sa.UniqueConstraint('Eye_color'),
    sa.UniqueConstraint('Films'),
    sa.UniqueConstraint('Gender'),
    sa.UniqueConstraint('Hair_color'),
    sa.UniqueConstraint('Heigh'),
    sa.UniqueConstraint('Homeworld'),
    sa.UniqueConstraint('Mass'),
    sa.UniqueConstraint('Name'),
    sa.UniqueConstraint('Skin_color'),
    sa.UniqueConstraint('Species'),
    sa.UniqueConstraint('Starships'),
    sa.UniqueConstraint('Url'),
    sa.UniqueConstraint('Vehicles')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=False),
    sa.Column('created', sa.String(length=120), nullable=False),
    sa.Column('diameter', sa.String(length=120), nullable=False),
    sa.Column('edited', sa.String(length=120), nullable=False),
    sa.Column('films', sa.String(length=120), nullable=False),
    sa.Column('gravity', sa.String(length=120), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('orbital_period', sa.String(length=120), nullable=False),
    sa.Column('population', sa.String(length=120), nullable=False),
    sa.Column('residents', sa.String(length=120), nullable=False),
    sa.Column('surface_water', sa.String(length=120), nullable=False),
    sa.Column('terrain', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('created'),
    sa.UniqueConstraint('diameter'),
    sa.UniqueConstraint('edited'),
    sa.UniqueConstraint('films'),
    sa.UniqueConstraint('gravity'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('orbital_period'),
    sa.UniqueConstraint('population'),
    sa.UniqueConstraint('residents'),
    sa.UniqueConstraint('surface_water'),
    sa.UniqueConstraint('terrain'),
    sa.UniqueConstraint('url')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Cargo_capacity', sa.String(length=120), nullable=False),
    sa.Column('consumables', sa.String(length=120), nullable=False),
    sa.Column('cost_in_credits', sa.String(length=120), nullable=False),
    sa.Column('created', sa.String(length=120), nullable=False),
    sa.Column('crew', sa.String(length=120), nullable=False),
    sa.Column('edited', sa.String(length=120), nullable=False),
    sa.Column('length', sa.String(length=120), nullable=False),
    sa.Column('manufacturer', sa.String(length=120), nullable=False),
    sa.Column('max_atmosphering_speed', sa.String(length=120), nullable=False),
    sa.Column('model', sa.String(length=120), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('passengers', sa.String(length=120), nullable=False),
    sa.Column('pilots', sa.String(length=120), nullable=False),
    sa.Column('films', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=120), nullable=False),
    sa.Column('vehicle_class', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Cargo_capacity'),
    sa.UniqueConstraint('consumables'),
    sa.UniqueConstraint('cost_in_credits'),
    sa.UniqueConstraint('created'),
    sa.UniqueConstraint('crew'),
    sa.UniqueConstraint('edited'),
    sa.UniqueConstraint('films'),
    sa.UniqueConstraint('length'),
    sa.UniqueConstraint('manufacturer'),
    sa.UniqueConstraint('max_atmosphering_speed'),
    sa.UniqueConstraint('model'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('passengers'),
    sa.UniqueConstraint('pilots'),
    sa.UniqueConstraint('url'),
    sa.UniqueConstraint('vehicle_class')
    )
    op.drop_table('zapatos')
    op.drop_table('vaqueros')
    op.drop_table('camisetas')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('name')

    op.create_table('camisetas',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('talla', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('color', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('marca', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='camisetas_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='camisetas_pkey')
    )
    op.create_table('vaqueros',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('talla', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('color', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('marca', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='vaqueros_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='vaqueros_pkey')
    )
    op.create_table('zapatos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('talla', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('color', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('marca', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='zapatos_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='zapatos_pkey')
    )
    op.drop_table('vehicles')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
