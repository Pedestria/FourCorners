package pedestria.fourcorners.world.level.block.entity;

import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.player.Inventory;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.inventory.AbstractContainerMenu;
import net.minecraft.world.level.block.state.BlockState;
import pedestria.fourcorners.registry.FCBlockEntities;
import pedestria.fourcorners.world.inventory.CoreFabricatorMenu;

public final class CoreFabricatorBlockEntity extends FCMenuBlockEntity {
    public CoreFabricatorBlockEntity(BlockPos pos, BlockState state) {
        super(FCBlockEntities.CORE_FABRICATOR_BLOCK_ENTITY.get(), pos, state, 10);
    }

    @Override
    public Component getDisplayName() {
        return blockTitle(getBlockState());
    }

    @Override
    public AbstractContainerMenu createMenu(int containerId, Inventory inventory, Player player) {
        return new CoreFabricatorMenu(containerId, inventory, this);
    }
}
