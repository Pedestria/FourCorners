package pedestria.fourcorners.world.inventory;

import net.minecraft.core.BlockPos;
import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.world.entity.player.Inventory;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.inventory.AbstractContainerMenu;
import net.minecraft.world.inventory.MenuType;
import net.minecraft.world.inventory.Slot;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraftforge.items.SlotItemHandler;
import pedestria.fourcorners.world.level.block.entity.FCMenuBlockEntity;

public abstract class FCMenuBase<T extends FCMenuBlockEntity> extends AbstractContainerMenu {
    protected final T blockEntity;
    protected final Level level;
    protected final BlockPos blockPos;

    protected FCMenuBase(MenuType<?> menuType, int containerId, Inventory inventory, T blockEntity) {
        super(menuType, containerId);
        this.blockEntity = blockEntity;
        this.level = inventory.player.level();
        this.blockPos = blockEntity.getBlockPos();
    }

    protected void addPlayerInventory(Inventory inventory, int leftCol, int topRow) {
        for (int row = 0; row < 3; row++) {
            for (int column = 0; column < 9; column++) {
                addSlot(new Slot(inventory, column + row * 9 + 9, leftCol + column * 18, topRow + row * 18));
            }
        }

        for (int column = 0; column < 9; column++) {
            addSlot(new Slot(inventory, column, leftCol + column * 18, topRow + 58));
        }
    }

    @Override
    public boolean stillValid(Player player) {
        return stillValid(
                net.minecraft.world.inventory.ContainerLevelAccess.create(level, blockPos),
                player,
                blockEntity.getBlockState().getBlock());
    }

    @Override
    public net.minecraft.world.item.ItemStack quickMoveStack(Player player, int index) {
        Slot sourceSlot = slots.get(index);
        if (!sourceSlot.hasItem()) {
            return net.minecraft.world.item.ItemStack.EMPTY;
        }

        net.minecraft.world.item.ItemStack sourceStack = sourceSlot.getItem();
        net.minecraft.world.item.ItemStack copiedStack = sourceStack.copy();
        int blockSlots = getMachineSlotCount();

        if (index < blockSlots) {
            if (!moveItemStackTo(sourceStack, blockSlots, slots.size(), true)) {
                return net.minecraft.world.item.ItemStack.EMPTY;
            }
        } else if (!moveItemStackTo(sourceStack, 0, blockSlots, false)) {
            return net.minecraft.world.item.ItemStack.EMPTY;
        }

        if (sourceStack.isEmpty()) {
            sourceSlot.set(net.minecraft.world.item.ItemStack.EMPTY);
        } else {
            sourceSlot.setChanged();
        }

        sourceSlot.onTake(player, sourceStack);
        return copiedStack;
    }

    protected abstract int getMachineSlotCount();

    @SuppressWarnings("unchecked")
    protected static <T extends FCMenuBlockEntity> T blockEntityFromNetwork(
            Inventory inventory, FriendlyByteBuf buffer, Class<T> blockEntityClass) {
        BlockPos pos = buffer.readBlockPos();
        BlockEntity blockEntity = inventory.player.level().getBlockEntity(pos);
        return (T) blockEntityClass.cast(blockEntity);
    }
}
