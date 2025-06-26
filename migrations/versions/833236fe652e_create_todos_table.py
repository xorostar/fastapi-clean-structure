"""create todos table

Revision ID: 833236fe652e
Revises: 45e06d63d60e
Create Date: 2025-06-26 23:59:25.864411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '833236fe652e'
down_revision: Union[str, Sequence[str], None] = '45e06d63d60e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Create todos table
    op.create_table('todos',
                    sa.Column('id', postgresql.UUID(
                        as_uuid=True), nullable=False),
                    sa.Column('user_id', postgresql.UUID(
                        as_uuid=True), nullable=False),
                    sa.Column('description', sa.String(), nullable=False),
                    sa.Column('due_date', sa.DateTime(), nullable=True),
                    sa.Column('is_completed', sa.Boolean(),
                              nullable=False, default=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('completed_at', sa.DateTime(), nullable=True),
                    sa.Column('priority', sa.String(),
                              nullable=False, default='Medium'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('todos')
