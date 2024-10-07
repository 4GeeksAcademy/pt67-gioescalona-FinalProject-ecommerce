"""empty message

Revision ID: 7c760dc6d511
Revises: e9aa5b96634a
Create Date: 2024-09-19 07:53:49.048327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c760dc6d511'
down_revision = 'e9aa5b96634a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('camisetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('talla', sa.String(length=10), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=False),
    sa.Column('marca', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vaqueros',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('talla', sa.String(length=10), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=False),
    sa.Column('marca', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('zapatos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('talla', sa.String(length=10), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=False),
    sa.Column('marca', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('zapatos')
    op.drop_table('vaqueros')
    op.drop_table('camisetas')
    # ### end Alembic commands ###
