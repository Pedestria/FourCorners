package pedestria.fourcorners.world.inventory;

import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.world.entity.player.Inventory;
import net.minecraftforge.items.SlotItemHandler;
import pedestria.fourcorners.registry.FCMenus;
import pedestria.fourcorners.world.level.block.entity.DimensionAccessorBlockEntity;

public final class DimensionAccessorMenu extends FCMenuBase<DimensionAccessorBlockEntity> {
    public DimensionAccessorMenu(
            int containerId, Inventory inventory, DimensionAccessorBlockEntity blockEntity) {
        super(FCMenus.DIMENSION_ACCESSOR_MENU.get(), containerId, inventory, blockEntity);

        addSlot(new SlotItemHandler(blockEntity.getItemHandler(), 0, 80, 20));
        addPlayerInventory(inventory, 8, 51);
    }

    public static DimensionAccessorMenu fromNetwork(
            int containerId, Inventory inventory, FriendlyByteBuf buffer) {
        return new DimensionAccessorMenu(
                containerId,
                inventory,
                blockEntityFromNetwork(inventory, buffer, DimensionAccessorBlockEntity.class));
    }

    @Override
    protected int getMachineSlotCount() {
        return 1;
    }
}
