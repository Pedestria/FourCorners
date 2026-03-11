package pedestria.fourcorners.registry;

import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import pedestria.fourcorners.FourCorners;
import pedestria.fourcorners.world.level.block.entity.CoreFabricatorBlockEntity;
import pedestria.fourcorners.world.level.block.entity.DimensionAccessorBlockEntity;

public final class FCBlockEntities {
    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITY_TYPES =
            DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, FourCorners.MODID);

    public static final RegistryObject<BlockEntityType<DimensionAccessorBlockEntity>>
            DIMENSION_ACCESSOR_BLOCK_ENTITY =
                    BLOCK_ENTITY_TYPES.register(
                            "dimension_accessor_block_entity",
                            () ->
                                    BlockEntityType.Builder.of(
                                                    DimensionAccessorBlockEntity::new,
                                                    FCBlocks.DIMENSION_ACCESSOR_BLOCK.get())
                                            .build(null));

    public static final RegistryObject<BlockEntityType<CoreFabricatorBlockEntity>>
            CORE_FABRICATOR_BLOCK_ENTITY =
                    BLOCK_ENTITY_TYPES.register(
                            "core_fabricator_block_entity",
                            () ->
                                    BlockEntityType.Builder.of(
                                                    CoreFabricatorBlockEntity::new,
                                                    FCBlocks.CORE_FABRICATOR_SIMPLE_BLOCK.get())
                                            .build(null));

    private FCBlockEntities() {}
}
